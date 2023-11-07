class Main inherits IO {
    a : Int <- 10;
    b : Int <- 5; 
    c : Int;
    d : Int;

    operation(num:Int) : Int {
        (let e : Int  in
	        {
                c <- 8;
                d <- 2;
                e <- (((num+b)/d)*a)-c;
                out_int(e);
	        }
        )
    };

    main() : Int {
        {
            (new Main).operation(5);
        }
    };
};

