class Main inherits IO {
    n: Int <- 5;
    t: Int;

    main() : Int {
        {(
            if n = 5 then
		        if n = 1 then
                    t <- 3
                else
                    t <- 4
                fi
            else
                if n = 2 then
                    t <- 1
                else
                    t <- 5
                fi
            fi
        );}
    };
};



