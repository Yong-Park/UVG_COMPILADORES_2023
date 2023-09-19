class Main inherits IO {
    a : Int <- 10;
    b : Int <- 5; 
    c : Int;
    d : Int;

    main() : Int {
    (let e : Int in
	 {
            c <- 8;
            d <- 2;
            e <- (a+b*c-d);
	 }
    )
    };
};

