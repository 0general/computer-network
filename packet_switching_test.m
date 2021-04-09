for N = 22:100
   syms g
   t = sym(nchoosek(N,g)*((0.2)^g)*((0.8)^(N-g)));
   P = symsum(t,g,21,N);
   
   N
   P  
   if (P>=0.01)
       break;
   end
end