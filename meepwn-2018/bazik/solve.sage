N = 101100845141156293469516586973179461987930689009763964117872470309684853512775295312081121501322683984914454311655512983781714534411655378725344931438891842226528067586198216797211681076517718505980665732445770547794541814618131322049740520275847849231052080791884055178607671253203354019327951368529475389269L
e = 3
c = 0x20375ebbb61e4841c9cb223fbbdd3bfc271fdfc581680ea1e8e6232b7a37a8d34e9979c0e0f44dac09efa840d8c3d74e59ec6477a2378221e7130d3b82602be37472df51621cc3e4b4be845c8c320051c9a712eafb50fe738c07bf01901d889981b3b0cea2abd3ef9771ae06de089791e83700627e2f8e5f83f17c082542a3da

m = 279194786064165631462403655571007005294665174222443770940031343055849950569774655464736942913588929603436045601725648607914699314619533463571673134L

P.<x> = PolynomialRing(Zmod(N), implementation='NTL')
f = (m + x)^e - c
roots = f.small_roots(epsilon=1/30)
for root in roots:
  num = int(m+root)
  msg = hex(num)[2:-1].decode('hex')
  print msg
