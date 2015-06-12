#include "source/fossa/fossa.h"

static void ev_handler(struct ns_connection * nc, int ev, void *)
{
  struct iobuf * io = &nc->recv_iobuf;

  switch (ev)
  {
    case NS_RECV:
      // This event handler implements simple TCP echo server
      ns_send(nc, io->buf, io->len);  // Echo received data back
      iobuf_remove(io, io->len);      // Discard data from recv buffer
      break;
    default:
      break;
  }
}

int main(void)
{
  struct ns_mgr mgr;

  ns_mgr_init(&mgr, NULL);

  // Note that many connections can be added to a single event manager
  // Connections can be created at any point, e.g. in event handler function
  ns_bind(&mgr, "1234", ev_handler, NULL);

  for (;;)
  {
    ns_mgr_poll(&mgr, 1000);
  }

  ns_mgr_free(&mgr);
  return 0;
}

