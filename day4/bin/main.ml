open Core   (* Arg parsing *)
open Stdio  (* In_channel - requires (libraries core) *)

type __passport = {
  byr: string;
  iyr: string;
  eyr: string;
  hgt: string;
  hcl: string;
  ecl: string;
  pid: string;
  cid: string option;
}

let id = function | Some(x) -> x | None -> "hi" (* ignore danger *)
let table = Hashtbl.create (module String)
let get table_ k = Hashtbl.find !table_ k
let set table_ k v = Hashtbl.set !table_ ~key:k ~data:v (* ; get table_ k |> function | Some(x) -> print_endline x | _ -> () *)
(* let set table_ k v = (print_endline @@ Printf.sprintf "Setting k:%s, v:%s" k v); Hashtbl.set table_ ~key:k ~data:v *)
let read file = In_channel.read_lines file
let passport = ref table
let count = ref 0

let reqs =
"byr"::
"iyr"::
"eyr"::
"hgt"::
"hcl"::
"ecl"::
"pid"::[]
let print_passport = Hashtbl.iter_keys !passport ~f:(fun x -> print_endline @@ Printf.sprintf "passport: %s" x)
let passport_check = List.for_all reqs ~f:(fun req -> (get passport req) |> function | Some(_) -> print_endline "true"; true | None -> false)
let newline_check str_ = if String.equal str_ "" then
begin print_passport; if passport_check then count := !count + 1 else passport := table; true end
else false

let parse_line line_ =
  let list_o_keypair = String.split line_ ~on:' ' in (* "a=1 b=2" -> [a=1; b=2] *)
  let key_pair = List.map list_o_keypair ~f:(String.split ~on:':') in (* [a=1; b=2] -> [[a;1];[b;2]] *)
  print_passport;
  List.iter key_pair ~f:(fun x -> if not @@ newline_check (id @@ List.nth x 0) then set passport (id @@ List.nth x 0) (id @@ List.nth x 1))

let parse_file file = List.iter (read file) ~f:(parse_line); print_endline @@ Printf.sprintf "Final tally: %d" !count

(* let print_lines f = List.iter (read f) ~f:print_endline *)
let filename_param = Command.Param.(anon ("filename" %: string))
let command =
  Command.basic
    ~summary:"Passport hacking"
    ~readme:(fun () -> "More detailed information")
    (Command.Param.map filename_param ~f:(fun filename ->
         (fun () -> parse_file filename)))

let () =
  Command.run ~version:"1.0" ~build_info:"RWO" command