#include <fossa.h>

static void ev_handler(struct ns_connection * nc, int ev, void *)
{
    struct mbuf * mbuf = &nc->recv_mbuf;

    switch (ev)
    {
        case NS_RECV:
            // This event handler implements simple TCP echo server
            ns_send(nc, mbuf->buf, mbuf->len);  // Echo received data back
            mbuf_remove(mbuf, mbuf->len);      // Discard data from recv buffer
            break;
        default:
            break;
    }
}

int main()
{
    struct ns_mgr mgr;

    ns_mgr_init(&mgr, nullptr);

    // Note that many connections can be added to a single event manager
    // Connections can be created at any point, e.g. in event handler function
    ns_bind(&mgr, "1234", ev_handler);

    for (;;)
    {
        ns_mgr_poll(&mgr, 1000);
    }

    ns_mgr_free(&mgr);
    return 0;
}

