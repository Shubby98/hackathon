##a=10
while true:
    import socket			 

    # next create a socket object
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)		 
    print ("Socket successfully created")

    port=3000
      
    s.bind(("0.0.0.0", port))		 
    print ("socket binded to %s" %(port))

        # put the socket into listening mode 
    s.listen(5)	 
    print ("socket is listening")		

            
    c, addr = s.accept()	 
    print ('Got connection from', addr )
            
            
    #t='done done'
            
    #c.send(t.encode())

    print(c.recv(1024))
    ##a=a-1

    s.close()      

         
