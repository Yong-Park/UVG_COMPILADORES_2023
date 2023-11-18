class Main inherits IO {
    n: Int <- 7;
    t: Int <- 3;

    main() : Int {
        {(
            out_int(n);
            if n = 5 then
            {
                t <- 2;
                out_int(t);
            }
            else
            {
                t <- 3;
                out_int(t);
            }
            fi
        );
        out_string("El valor de n es: \n");
        out_int(n);
        }
    };
};
    


