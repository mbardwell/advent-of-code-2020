open Core
open Stdio

let read file = In_channel.read_lines file
let print_list list_ = print_endline "starting list"; List.iter list_ ~f:(print_endline); print_endline "end of list"

let groups = ref []
let rec to_groups group = function
| h::t ->
  if String.equal h "" then
    begin
    print_list group;
    groups := List.append !groups [group];
    to_groups [] t
    end
  else
    to_groups (List.append group [h]) t
| [] -> ()

let stringify group = List.fold group ~init:"" ~f:(^)

let _count = ref 0
let _unique = ref []
let rec unique = function
| char_::t -> if not @@ List.exists !_unique ~f:(fun x -> Char.equal x char_) then _unique := List.append !_unique [char_]; unique t
| [] -> print_endline @@ Printf.sprintf "unique length: %d" @@ List.length !_unique; _count := !_count + (List.length !_unique); _unique := []

let solve lines =
  let () = to_groups [] lines in
  let groups_s = List.map !groups ~f:stringify in
  List.iter groups_s ~f:(fun x -> String.to_list x |> unique);
  Printf.printf "count %d\n" !_count

let _count2 = ref 0
let everyone_yes group =
  let char_in_str str_ char_ = String.exists str_ ~f:(fun char_' -> Char.equal char_ char_' )  in
  let char_for_all char_ = List.for_all group ~f:(fun x -> char_in_str x char_) in
  let all_chars = stringify group in
  List.iter (String.to_list all_chars) ~f:(fun x -> if (char_for_all x) then _count2 := !_count2 + 1)

let solve2 lines =
  let () = to_groups [] lines in
  List.iter !groups ~f:(fun x -> everyone_yes x);
  Printf.printf "count %d\n" !_count2

let filename_param = Command.Param.(anon ("filename" %: string))
let command =
  Command.basic
    ~summary:"Passport hacking"
    ~readme:(fun () -> "More detailed information")
    (Command.Param.map filename_param ~f:(fun filename ->
         (fun () -> solve2 (read filename))))

let () =
  Command.run ~version:"1.0" ~build_info:"RWO" command