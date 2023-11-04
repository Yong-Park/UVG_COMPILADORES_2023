class Main inherits IO {
    a : Int <- 3;
    b : Int <- 3; 
    c : Int;

    main() : Object {
	    {
        (
        while b = a loop
	        {
                a <- a + b;
	        }
        pool
	
        );
	    }
    };
};