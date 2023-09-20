class Main inherits IO {
    n: Int <- 5;
    t: Int;

    main() : Int {
        {(
            if n = 5 then
                t <- (n+8) / n
            else
                t <- 5/n
            fi
        );}
    };
};


