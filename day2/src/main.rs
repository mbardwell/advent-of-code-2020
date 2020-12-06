use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind};
use std::process;

fn read(path: &str) -> Result<Vec<Vec<&str>>, Error> {
    //https://users.rust-lang.org/t/reading-integers-from-a-file-into-vector/17517/5
    let file = File::open(path)?; // open file by given path
    // wrap file into generic buffered reader, it will use 4 KB buffer internally
    // to reduce number of syscalls, thus improving performance
    let br = BufReader::new(file);
    // create an empty vector, type of the stored elements will be inferred
    let mut resp = Vec::new();
    // br.lines() creates an iterator over lines in the reader
    // see: https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines
    for line in br.lines() {
        // IO operations generally can return error, we check if got
        // an error,in which case we return this error as the function result
        let line = line?;
        let v: Vec<&str> = line   
            .trim() // trim "whitespaces"
            .split(": ")
            .collect(); // 
            //.map_err(|e| Error::new(ErrorKind::InvalidData, e))?; // parse() can return error (e.g. for string "abc"), here if we got it, we convert it to `std::io::Error` type and return it as function result
        resp.push(v); 
    }
    Ok(resp) // everything is Ok, return vector
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = parse_config(&args);
    println!("file {}", filename);
    let contents = read(filename).unwrap_or_else(|err| {
        println!("read error: {}", err);
        process::exit(1);
    });
}

fn parse_config(args: &[String]) -> &str {
    let filename = &args[1];
    return filename;
}
