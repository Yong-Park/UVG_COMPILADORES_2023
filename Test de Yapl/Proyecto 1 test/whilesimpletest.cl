class Main inherits IO {
    a : Int <- 10;
    b : Int <- 5; 
    c : Int;

    main() : Object {
	    {
        (
        while b = a loop
	        {
                c <- a + 2;
	            b <- c;
	        }
        pool
	
        );
	    }
    };
};