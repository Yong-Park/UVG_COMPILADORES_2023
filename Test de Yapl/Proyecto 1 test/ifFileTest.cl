class Main inherits IO {
    n: Int <- 4;
    t: Int <- 1;

    main() : Int {
        {(
            if n = 5 then
                n <- 3
            else
                if t = 3 then
                    n <- 1
                else
                    n <- 10
                fi
            fi
        );}
    };
};
    


