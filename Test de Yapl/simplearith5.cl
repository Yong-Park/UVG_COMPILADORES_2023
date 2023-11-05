class Main inherits IO {
    a : Int <- 4;
    b : Int <- 2;
    d : Int <- 8;

    main(s : Int) : Int {
    (let c : Int  in
	 {
            c <- ((d+a)/b);
            out_int(c)
	 }
    )
    };
};