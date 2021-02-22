function abs(v) {return v < 0 ? -v : v}
BEGIN{ s1=s2=s3=0 }
{
  v=$1
  a = abs(v-2.433055879794988)
  if( a < 0.001 ) {
    s1 = s1 + 1
  }
  b = abs(v-3.2639296187683287)
  if( b < 0.001 ) {
    s2 = s2 + 1
  }
  c = abs(v-6.527859237536657)
  if( c < 0.001 ) {
    s3 = s3 + 1
  }
}
END {
  print s1, s2, s3
}
