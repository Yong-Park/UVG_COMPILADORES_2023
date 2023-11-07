class Main inherits IO {
    n: Int <- 7;
    t: Int <- 3;

    main() : Int {
        {(
            if n = 5 then
            {
                t <- 2;
                out_int(t);
            }
            else
            {
                if t = 3 then
                {
                    t <- 4;
                    out_int(t);
                }
                else
                {
                    t <- 5;
                    out_int(t);
                }
                fi
            }
            fi
        );
        out_string("El valor de n es: \n");
        out_int(n);
        }
    };
};
    


