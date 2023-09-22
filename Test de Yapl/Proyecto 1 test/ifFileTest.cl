class Main inherits IO {
    n: Int <- 5;
    t: Int;

    main() : Int {
        {(
            if n = 5 then
		        t <- 2
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



