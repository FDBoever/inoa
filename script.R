#!/usr/bin/env Rscript
args = commandArgs(trailingOnly=TRUE)

if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
} else if (length(args)==1) {
  # default output file
  args[2] = "out.txt"
} else{
  input=args[1]
  output=args[2]
}


message("R succesfully loaded")
message("input: ", input)
message("output: ", output)
