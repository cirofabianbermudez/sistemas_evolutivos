function abs(v) {return v < 0 ? -v : v}
{
  v=$1
  a = abs(v- 3.652887442162178)
  if( a < 0.0001 ) {
    s1 = s1 + 1
  }
}
END {
  print s1
}
