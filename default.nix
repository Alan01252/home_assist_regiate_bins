with import <nixpkgs> {};

(
    let

    QueryableList = python38.pkgs.buildPythonPackage rec {
        pname = "QueryableList";
        version = "3.1.0";

        src = python38.pkgs.fetchPypi {
            inherit pname version;
            sha256 = "1s8inksli95707ii7y9sm8i4a8nvz3c2c62fjkskb6n6mp5xr4c8";
        };

        doCheck = false;
    };


    
    AdvancedHTMLParser = python38.pkgs.buildPythonPackage rec {
        pname = "AdvancedHTMLParser";
        version = "9.0.1";

        src = python38.pkgs.fetchPypi {
            inherit pname version;
            sha256 = "0dw88pcblz7ymqkranxjsl3mr4cp5c8q8v49xr8cl7y6lhn66zqv";
        };

        doCheck = false;

	propagatedBuildInputs = [ QueryableList ];

    };

   


    in python38.withPackages (ps: [ 
	AdvancedHTMLParser
	ps.requests
    ]
)).env
