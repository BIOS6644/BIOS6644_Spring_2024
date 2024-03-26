###########################################
# Code for Mendeley for Cell Metabolism submission, 4/26/2018
###########################################

library(Hmisc)
library(sandwich)
library(xlsx)
library(mice)
library(lme4)
library(GenABEL)
# setwd("Y:/SUGAR/Analyses/SUGAR metabolomics insulin sensitivity/Code and data for Cell Metabolism") # change this path to local directory that contains data files!
source("myvolcano.R")
source("lmer_lincom.R")

# main dataset
dat.ori <- read.csv(file="main_data_for_mendeley.csv", header=T)

# load fasting plasma data
plasma <- read.csv(file="fasting_plasma_data_for_mendeley.csv", header=T)
# and merge with patient-level data
plasma <- merge(plasma, dat.ori, by="patient", all.x=T); dim(plasma) # 93 132

###########################################
# Associations of metabolite with CKD
###########################################
# do regressions of metabolite on fasting metabolite on CKD for plasma, lipids, and urine
# plasma
dat <- plasma
z1 <- p1 <- betastd1 <- bbeta1 <- ci.lower1 <- ci.upper1 <- array(NA, dim=124)
metcol <- 2 # column where metabolites start
for(i in metcol:(metcol+length(z1)-1)) # 74 measured metabolites
{
  mod1 <- lm(dat[,i] ~ dat$ckd + dat$age + dat$male + dat$white + dat$weightscreen)
  v1 <- vcovHC(mod1, type="HC0")
  bbeta1[i-(metcol-1)] <- mod1$coef[2]
  ci.lower1[i-(metcol-1)] <- mod1$coef[2] - 1.96*sqrt(diag(v1))[2]
  ci.upper1[i-(metcol-1)] <- mod1$coef[2] + 1.96*sqrt(diag(v1))[2]
  z <- mod1$coef[2]/sqrt(diag(v1))[2]
  betastd1[i-(metcol-1)] <- z # start at 1 (standardized beta coefficient)
  p1[i-(metcol-1)] <- 2*(1-pnorm(abs(z)))
  names(p1)[i-(metcol-1)] <- names(betastd1)[i-(metcol-1)] <-
    names(z1)[i-(metcol-1)] <- colnames(dat)[i]
}

# Figure 1: volcano plot of % in change in metabolite with CKD
par(mar=c(5,5,1,1))
myvolcano(bbeta1, p1, main="", cex.lab=1.7, cex.axis=1.7, cex.main=1.7, xlim=c(0.15, 5), ylim=c(0,16))

# Control FDR at 10%
pres.ckd <- cbind(round(cbind(100*(exp(bbeta1)-1), 100*(exp(ci.lower1)-1), 100*(exp(ci.upper1)-1)), 2), p1)
pres.ckd.ord <- pres.ckd[order(pres.ckd[,4]),]

# Tables for CKD
fdr1 <- data.frame(j=1:124)
fdr1$thresh <- 0.10*fdr1$j/124
p1yn <- ifelse(pres.ckd.ord[,4] < fdr1$thresh, 1, 0); table(p1yn)
names(p1yn)[p1yn==1] # these are the 59 plasma metabolites that pass the FDR threshhold for CKD
res1 <- cbind(pres.ckd.ord, fdrthresh=fdr1$thresh, p1yn)
res1 <- as.data.frame(res1[order(res1[,1]),])
qval <- qvaluebh95(res1[,4], fdrate=0.1)  # get q-value (not just FDR threshold)
res1 <- cbind(res1, qval)
res1$out <- apply(res1[,1:3], 1, function(x){x <- round(x); paste(x[1], " (", x[2], ", ", x[3], ")", sep="")})
res1 <- res1[order(res1$V1, decreasing=T), ]
write.csv(res1[,c("out", "p1", "qvalue")], file="table2_cell_metabolism.csv")

##########################################################
# Associations of metabolite with insulin infusion
##########################################################
plcms <- read.csv(file="clamp_plasma_data_for_mendeley.csv", header=T); dim(plcms)
plasma <- merge(plcms, dat.ori, by="patient", all.x=T); dim(plasma)

# do comparisons of clamp v. fast for plasma 
z1 <- p1 <- betastd1 <- bbeta1 <- ci.lower1 <- ci.upper1 <- array(NA, dim=74)

# Plasma clamp
plasma$samptype <- ifelse(is.element(plasma$samptype, "clamp"), 1, 0) #"time" var.
dat <- plasma

metcol <- 4 # column where metabolites start
for(i in metcol:(metcol+length(z1)-1)) # 74 measured metabolites
{
  mod1 <- lmer(dat[,i] ~ samptype + age + male + white + weightscreen + batch + (1|patient), data=dat)
  v1 <- vcov(mod1)
  bbeta1[i-(metcol-1)] <- fixef(mod1)[2]
  ci.lower1[i-(metcol-1)] <- fixef(mod1)[2] - 1.96*sqrt(diag(v1))[2]
  ci.upper1[i-(metcol-1)] <- fixef(mod1)[2] + 1.96*sqrt(diag(v1))[2]
  z <- fixef(mod1)[2]/sqrt(diag(v1))[2]
  betastd1[i-(metcol-1)] <- z # start at 1 (standardized beta coefficient)
  p1[i-(metcol-1)] <- 2*(1-pnorm(abs(z)))
  names(p1)[i-(metcol-1)] <- names(betastd1)[i-(metcol-1)] <-
    names(z1)[i-(metcol-1)] <- colnames(dat)[i]
}

# Table 3
pcres <- cbind(round(cbind(100*(exp(bbeta1)-1), 100*(exp(ci.lower1)-1), 100*(exp(ci.upper1)-1)), 2), p1)

p1ord <- p1[order(p1)]

fdr1 <- data.frame(j=1:74)
fdr1$thresh <- 0.10*fdr1$j/74
p1yn <- ifelse(p1ord < fdr1$thresh, 1, 0); table(p1yn)
names(p1yn)[p1yn==1] # these are the 66 plasma metabolites that pass the FDR threshhold for plasma clamp
dim(pcres[rownames(pcres) %in% names(p1yn)[p1yn==1],])
res1 <- cbind(pcres, fdrthresh=fdr1$thresh)
res1 <- as.data.frame(res1); res1 <- res1[order(res1[,1]),]
res1$p1yn <- res1$p1 < res1$fdrthresh
qval <- qvaluebh95(res1[,4], fdrate=0.1)  # update to get q-value (not just FDR threshold)
res1 <- cbind(res1, qval)
res1$out <- apply(res1[,1:3], 1, function(x){x <- round(x); paste(x[1], " (", x[2], ", ", x[3], ")", sep="")})
write.csv(res1[,c("out", "p1", "qvalue")], file="table3_cell_metabolism.csv")

#################################################
# Now, does CKD modify pre-post association?
#################################################
plasnames <- names(plasma)[4:77]

table4 <- matrix(NA, nrow=length(plasnames), ncol=3)
counter <- 1
for(i in plasnames){
  dat <- plasma
  mod1 <- lmer(dat[,colnames(dat) %in% i] ~ samptype + ckd + samptype*ckd + age + male + white + weightscreen
    + batch + (1|patient), data=dat)
  temp <- c(
    lmer.lincom(mod1, c("samptype"), exp=T)[1], # time trend for non CKD
    lmer.lincom(mod1, c("samptype", "samptype:ckd"), exp=T)[1], # time trend for CKD
    lmer.lincom(mod1, c("samptype:ckd"), exp=T)[2] # p-value for interaction
    )
  table4[counter,] <- temp
  counter <- counter + 1
}
colnames(table4) <- c("clamp effect, >=60", "clamp effect, <60", "clamp int p")
rownames(table4) <- plasnames
table4 <- table4[order(table4[,"clamp int p"]),]
write.csv(table4, file="table4_cell_metabolism.csv")














