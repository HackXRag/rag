#!/usr/bin/perl

while(<>){
  print "$1" if /(Avg prompt throughput: \d+\.*\d* tokens\/s, Avg generation throughput: \d+\.*\d* tokens\/s, Running: \d+ reqs)/;
  if (/Avg prompt throughput: (\d+\.*\d*) tokens\/s, Avg generation throughput: \d+\.*\d* tokens\/s, Running: \d+ reqs/)
  {
	  $sum = $sum + $1;
	  $count = $count + 1;
	  print ("\t", $sum/$count, "\n");
  }
}
