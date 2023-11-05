class Main inherits IO {
    a : Int <- 3;
    b : Int <- 3; 
    c : Int;

    main() : Object {
	    {
        (
        while b = a loop
	        {
                while a = 3 {
                    a <- a + b;
                }
                
	        }
        pool
	
        );
	    }
    };
};