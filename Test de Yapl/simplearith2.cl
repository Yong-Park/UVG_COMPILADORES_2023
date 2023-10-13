class Main inherits IO {
    a : Int <- 10;
    b : Int <- 2;

    main(s : Int) : Int {
    (let c : Int  in
	 {
            c <- a/b;
	 }
    )
    };
};