class Main inherits IO {
    a : Int <- 3;
    b : Int <- 3; 
    c : Int;

    main() : Object {
	    {
        (
        while b = a loop
	        {
              (
                while b = a loop
                    {
                        out_int(a);
                        a <- a + b;
                        out_int(a);
                    }
                pool
                
                );
	        }
        pool
        
        );
        out_int(a);
	    }
    };
};

