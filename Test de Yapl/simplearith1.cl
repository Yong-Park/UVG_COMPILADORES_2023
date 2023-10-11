class Main inherits IO {
    a : Int <- 100;
    b : Int <- 515; 

    main(s : Int) : Int {
    (let c : Int  in
	 {
            c <- a+b;
	 }
    )
    };
};