class Main inherits IO {
    a : Int <- 10;
    b : Int <- 2;
    d : Int; 

    main(s : Int) : Int {
    (let c : Int <- 5  in
	 {
            d <- (c*a-b) / 8;
	 }
    )
    };
};