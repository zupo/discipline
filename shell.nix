let
  # Freeze nixpkgs version
  nixpkgs = builtins.fetchTarball {
    # taken from https://github.com/NixOS/nixpkgs/tree/nixos-22.05 on 2022-06-03
    url = "https://github.com/nixos/nixpkgs/archive/7ba0bb440c4d4483225dde894e523270949f32d3.tar.gz";
    sha256 = "0h1ljhybv6qvqaj2ya5v4k1ri5c7hrp00f7s3xslkmilwj95cz66";
  };
  pkgs = import nixpkgs {};

  # Poetry-based dev environment
  devEnv = pkgs.poetry2nix.mkPoetryEnv {
    projectDir = ./.;
    python = pkgs.python310;
  };
in

pkgs.mkShell {
  name = "dev-shell";
  buildInputs = [
    pkgs.python310
    pkgs.poetry

    devEnv
  ];
}
