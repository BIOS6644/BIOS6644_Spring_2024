mSet<-InitDataObjects("conc", "pathqea", FALSE)
mSet<-Read.TextData(mSet, "Replacing_with_your_file_path", "rowu", "disc");
mSet<-CrossReferencing(mSet, "name");
mSet<-PerformDetailMatch(mSet, "Phosphoglyceric Acid");
mSet<-GetCandidateList(mSet);
mSet<-SetCandidate(mSet, "Phosphoglyceric Acid", "2-Phosphoglyceric acid");
mSet<-PerformDetailMatch(mSet, "Acetylcholine");
mSet<-GetCandidateList(mSet);
mSet<-SetCandidate(mSet, "Acetylcholine", "Acetylcholine ");
mSet<-PerformDetailMatch(mSet, "D-Glucoronic acid");
mSet<-GetCandidateList(mSet);
mSet<-SetCandidate(mSet, "D-Glucoronic acid", "D-Glucuronic acid");
mSet<-SanityCheckData(mSet)
mSet<-RemoveMissingPercent(mSet, percent=0.5)
mSet<-ImputeVar(mSet, method="min")
mSet<-Normalization(mSet, "NULL", "NULL", "AutoNorm", "20", ratio=FALSE, ratioNum=20)
mSet<-PlotNormSummary(mSet, "norm_0_", "png", 72, width=NA)
mSet<-PlotSampleNormSummary(mSet, "snorm_0_", "png", 72, width=NA)
mSet<-SetKEGG.PathLib(mSet, "hsa")
mSet<-SetMetabolomeFilter(mSet, F);
mSet<-CalculateQeaScore(mSet, "rbc", "gt")
mSet<-PlotPathSummary(mSet, "path_view_0_", "png", 72, width=NA)
mSet<-GetCircleInfo(mSet)
mSet<-PlotMetPath(mSet, "Ubiquinone and other terpenoid-quinone biosynthesis", 480, 460)
mSet<-PlotMetPath(mSet, "Phenylalanine, tyrosine and tryptophan biosynthesis", 480, 460)
mSet<-PlotMetPath(mSet, "Caffeine metabolism", 480, 460)
mSet<-SaveTransformedData(mSet)
mSet<-GetCircleInfo(mSet)
mSet<-PlotMetPath(mSet, "Ubiquinone and other terpenoid-quinone biosynthesis", 480, 460)
mSet<-PlotMetPath(mSet, "Ubiquinone and other terpenoid-quinone biosynthesis", 480, 460)
mSet<-PlotMetPath(mSet, "Ubiquinone and other terpenoid-quinone biosynthesis", 480, 460)
mSet<-PlotMetPath(mSet, "Ubiquinone and other terpenoid-quinone biosynthesis", 480, 460)
mSet<-PlotMetPath(mSet, "Tyrosine metabolism", 480, 460)
mSet<-PlotMetPath(mSet, "Arginine and proline metabolism", 480, 460)
mSet<-PlotMetPath(mSet, "Citrate cycle (TCA cycle)", 480, 460)
mSet<-PlotMetPath(mSet, "Inositol phosphate metabolism", 480, 460)
mSet<-PlotMetPath(mSet, "Glycerophospholipid metabolism", 480, 460)
mSet<-PlotMetPath(mSet, "Pyrimidine metabolism", 480, 460)
mSet<-PlotMetPath(mSet, "Galactose metabolism", 480, 460)
mSet<-PlotMetPath(mSet, "Alanine, aspartate and glutamate metabolism", 480, 460)
mSet<-PlotMetPath(mSet, "Glycine, serine and threonine metabolism", 480, 460)
mSet<-PlotMetPath(mSet, "Inositol phosphate metabolism", 480, 460)
mSet<-SaveTransformedData(mSet)
