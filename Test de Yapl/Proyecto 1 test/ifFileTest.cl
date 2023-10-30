class Main inherits IO {
    n: Int <- 5;
    t: Int;

    main() : Int {
        {(
            if n = 5 then
                t <- 3
            else
                t <- 1
            fi
        );}
    };
};
    


