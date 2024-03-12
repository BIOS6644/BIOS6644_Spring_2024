# will return est (95% CI) and pvalue for any linear combination of parameters
lmer.lincom <- function(mod, terms.index, lincom=NULL, alpha=0.05, exp=F, digits=2){
  if(is.null(lincom)){lincom <- rep(1, length(terms.index))}

  est <- lincom %*% fixef(mod)[names(fixef(mod)) %in% terms.index]
  v <- t(lincom) %*% vcov(mod)[names(fixef(mod)) %in% terms.index, names(fixef(mod)) %in% terms.index] %*% lincom
  ci.lower <- est + qnorm(alpha/2) %o% sqrt(diag(v))
  ci.upper <- est + qnorm(1-alpha/2) %o% sqrt(diag(v))
  p <- 2*(1-pnorm(abs(est/sqrt(diag(v)))))
  p <- ifelse(p < 0.001, "< 0.001", signif(p, digits))

  if(exp){res <- c(paste(round(exp(est), digits), " (", round(exp(ci.lower), digits), ", ",
    round(exp(ci.upper), digits), ")", sep=""), p)
  } else {res <- c(paste(round(est, digits), " (", round(ci.lower, digits), ", ", round(ci.upper, digits), ")", sep=""),
    p)}

  return(res)
}