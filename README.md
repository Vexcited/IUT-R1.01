# R1.01

Solutions are written in the following languages:

- Python (the one we should use originally during the TPs)
- French pseudo code (files with `.fr` extension), because I'm French and the teacher wants us to resolve the TDs in pseudo code. Interpreter used will be [`frr`](https://github.com/Vexcited/frr).
- [Rust](https://www.rust-lang.org/)
- [Zig](https://ziglang.org/)
- C

## Usage

If the language used produces a binary, make sure that the binary is executable, if not run `chmod +x ./bin_file`.

### C

```bash
# We compile using gcc
gcc ./file.c -o c_bin && ./c_bin
```

### Rust

```bash
# We compile using rustc
rustc ./file.rs -o rust_bin && ./rust_bin
```

### Zig

We can directly run the file using `zig run ./file.zig`.

But if we want to compile it, we can do the following:

```bash
zig build-exe --name zig_bin ./file.zig && ./zig_bin
```

Note that the binary will be in mode `Debug` by default, so no optimisations will be made.
Otherwise, use the `-O ReleaseSafe` flag.

### Python

Only Python 3 is supported.

```bash
# We run the python file
python3 ./file.py
```
