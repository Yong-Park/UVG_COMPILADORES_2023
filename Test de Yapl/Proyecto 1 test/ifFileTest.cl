class Main inherits IO {
    n: Int <- 7;
    t: Int <- 3;

    main() : Int {
        {(
            if n = 5 then
            {
                t <- 3;
                out_int(t);
            }
            else
            {
                t <- 1;
                out_int(t);
            }
            fi
        );
        out_string("El valor de n es: ");
        out_int(n);
        }
    };
};
    


