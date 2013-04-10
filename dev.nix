{ }:

let
  base = import ./base.nix { };

in

with import <nixpkgs> {};

buildEnv {
  name = "dev-env";
  paths =
    [ python27Packages.sqlalchemy
    ] ++ base.paths27;
}