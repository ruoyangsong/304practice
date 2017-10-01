#super slow run time if we do it by recurssive
def cut_rod(p,n):
  if n==0:
    return 0
  q = -float("inf")
  for i in range(1,n+1):
    q = max(q,p[i]+cut_rod(p,n-i))
    #print q   
  return q

def dynamic_cut_rod(p,n):
  r = [None for x in range(n+1)]
  s = [None for x in range(n+1)]
  r[0] = 0
  s[0] = 0
  for j in range (1,n+1):
    q = -float("inf")
    for i in range(1,j+1):
     # print "p[i]+r[j-i] is %d"%p[i]+r[j-i]    
      if q<(p[i]+r[j-i]):
        q = p[i]+r[j-i]
	s[j] = i
    r[j] = q
  return (r,s)

def print_sol(p,n):
  (r,s) = dynamic_cut_rod(p,n)
  while n>0:
    print s[n]
    n = n-s[n]

if __name__=="__main__":
  price = [0,1,5,8,9,10,17,17,20,24,30]
  #print "length is %d"%price[0]
  length = 10
  #print(dynamic_cut_rod(price,length))
  print_sol(price,length)
