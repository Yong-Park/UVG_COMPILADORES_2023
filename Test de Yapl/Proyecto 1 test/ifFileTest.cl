class Main inherits IO {
    n: Int <- 5;
    t: Int <- 3;

    main() : Int {
        {(
            if n = 5 then
                n <- 3
            else
                n <- 1
            fi
        );}
    };
};
    


