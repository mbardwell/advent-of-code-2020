open Lwt
open Lwt_io

let ping obj msg =
  let%lwt () = printlf "received: %s" msg in
  return msg

let interface =
  Mylib.Ping_pong.Org_foo_bar.make {
    Mylib.Ping_pong.Org_foo_bar.m_Ping = (fun obj msg -> ping (OBus_object.get obj) msg);
  }

let () = Lwt_main.run begin
  let%lwt bus = OBus_bus.session () in

  (* Request a name *)
  let%lwt _ = OBus_bus.request_name bus "org.plop" in

  (* Create the object *)
  let obj = OBus_object.make ~interfaces:[interface] ["plip"] in
  OBus_object.attach obj ();

  (* Export the object on the connection *)
  OBus_object.export bus obj;

  (* Wait forever *)
  fst (wait ())
end