use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind};
use std::process;

fn find_sum(sum: i32, arr: Vec<i32>) {
    for outer in &arr {
        for inner in &arr {
            if (outer + inner) == sum {
                println!("The answer is {}", outer*inner);
            }
        }
    }
}

fn find_sum3(sum: i32, arr: Vec<i32>) {
    for outer in &arr {
        for inner in &arr {
            for more_inner in &arr {
                if (outer + inner + more_inner) == sum {
                    println!("The 3 answer is {}", outer*inner*more_inner);
                }
            }
        }
    }
}

fn read(path: &str) -> Result<Vec<i32>, Error> {
    //https://users.rust-lang.org/t/reading-integers-from-a-file-into-vector/17517/5
    let file = File::open(path)?; // open file by given path
    // wrap file into generic buffered reader, it will use 4 KB buffer internally
    // to reduce number of syscalls, thus improving performance
    let br = BufReader::new(file);
    // create an empty vector, type of the stored elements will be inferred
    let mut v = Vec::new();
    // br.lines() creates an iterator over lines in the reader
    // see: https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines
    for line in br.lines() {
        // IO operations generally can return error, we check if got
        // an error,in which case we return this error as the function result
        let line = line?;
        let n = line   
            .trim() // trim "whitespaces"
            .parse() // call `str::parse::<i64>(&self)` method on the trimmed line, which parses integer
            .map_err(|e| Error::new(ErrorKind::InvalidData, e))?; // parse() can return error (e.g. for string "abc"), here if we got it, we convert it to `std::io::Error` type and return it as function result
        v.push(n); // push acquired integer to the vector
    }
    Ok(v) // everything is Ok, return vector
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let (sum, filename) = parse_config(&args);
    println!("Sum: {}, file {}", sum, filename);
    let contents = read(filename).unwrap_or_else(|err| {
        println!("read error: {}", err);
        process::exit(1);
    });
    find_sum(sum, contents);
    let contents = read(filename).unwrap_or_else(|err| {
        println!("read error: {}", err);
        process::exit(1);
    });
    find_sum3(sum, contents);
}

fn parse_config(args: &[String]) -> (i32, &str) {
    let sum = &args[1].parse().expect("Not a number!");
    let filename = &args[2];
    (*sum, filename)
}

