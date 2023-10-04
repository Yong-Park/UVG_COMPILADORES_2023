class Main inherits IO {
    a : Int <- 10;
    b : Int <- 5; 
    c : Int;
    f : String;
    d : Int;

    main(s : Int) : Int {
    (let e : Int <- 6 in
	 {
            c <- 8;
            d <- 2;
            e <- (a+b*c-d)/(b*c-a);
	 }
    )
    };
};

