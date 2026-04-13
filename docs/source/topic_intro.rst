Introduction into HTTP
**********************

.. note::
    This section is still under development. If you would like to contribute, feel free to
    `open a Pull Request <https://github.com/balder-dev/balderhub-http/pulls>`_.

HTTP is a stateless protocol for web communication, likely operating on a request-response model.

Resources are identified by URIs, with methods like GET and POST defining actions.

The evidence leans toward HTTP having versions like 1.1, 2, and 3, each with performance enhancements.

This BalderHub package should following RFC's:

* `RFC 9110: HTTP Semantics <https://www.rfc-editor.org/rfc/rfc9110>`_
* `RFC 9112: HTTP/1.1 <https://www.rfc-editor.org/rfc/rfc9112>`_

Overview
========

HTTP, or Hypertext Transfer Protocol, is the backbone of web communication, enabling data exchange between clients
(like browsers) and servers. It operates on a stateless, request-response model, meaning each request is independent,
and the server responds to each without retaining prior interaction details.

How HTTP Works
--------------

In HTTP, a client sends a request to a server, specifying:

**Method:** The action, such as GET to retrieve data or POST to submit it.

**URI:** Identifies the resource, like a webpage or file.

**Headers:** Provide additional information, like content type or language preferences.

The server processes this and returns a response with:

**Status Code:** Indicates success (e.g., 200 OK) or failure (e.g., 404 Not Found).

**Headers:** Metadata about the response.

**Body:** The actual data, like HTML content or an image.

Versions and Features
---------------------

HTTP has evolved, with versions like:

**HTTP/1.1:** Introduced persistent connections for efficiency.

**HTTP/2:** Added multiplexing and header compression for faster performance.

**HTTP/3:** Uses QUIC for reduced latency, enhancing reliability.

It also supports content negotiation, allowing clients and servers to agree on data formats, and caching to store
responses for reuse, improving speed and reducing server load. For secure communication, HTTP can use TLS, known as
HTTPS, encrypting data to protect against eavesdropping.

For detailed specifications, refer to the official RFC documents:

* `RFC 9110: HTTP Semantics <https://www.rfc-editor.org/rfc/rfc9110>`_
* `RFC 9112: HTTP/1.1 <https://www.rfc-editor.org/rfc/rfc9112>`_
* `RFC 9113: HTTP/2 <https://www.rfc-editor.org/rfc/rfc9113>`_
* `RFC 9114: HTTP/3 <https://www.rfc-editor.org/rfc/rfc9114>`_

Comprehensive Analysis of HTTP Operations
=========================================

This section provides an in-depth exploration of the Hypertext Transfer Protocol (HTTP), detailing its mechanisms,
evolution, and technical specifications, particularly referencing the relevant Request for Comments (RFC) documents.

Introduction to HTTP
--------------------

HTTP, first specified in the early 1990s, is a stateless, application-level protocol designed for distributed,
collaborative, hypertext information systems. As outlined in
`RFC 9110: HTTP Semantics <https://www.rfc-editor.org/rfc/rfc9110>`_, it is a family of request/response protocols
sharing a generic interface, extensible semantics, and self-descriptive messages. This design enables flexible
interaction, hiding implementation details and presenting a uniform interface to clients, independent of resource types.
The protocol's focus on communication syntax, intent, and expected recipient behavior, as noted in the introduction,
emphasizes observable interface changes, supporting intermediation through proxies and gateways for translating
non-HTTP systems.

Core Operational Mechanisms
---------------------------

HTTP operates on a request-response model, where clients initiate communication by sending HTTP requests to servers,
which respond accordingly.

The key components, detailed in `RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110>`_, include:

**Resources and URIs:** Resources, the targets of HTTP requests, are identified by Uniform Resource Identifiers (URIs),
as per Section 3.1 of RFC 9110. This identification allows precise location and access, crucial for web navigation.

**Methods:**

HTTP defines a set of request methods indicating the desired action on a resource. Common methods, as referenced in
RFC 9110, include:

* ``GET:`` Retrieve a representation (Section 9.3.1).

* ``POST:`` Submit data for processing (Section 9.3.3).

* ``PUT:`` Update with provided representation (Section 9.3.4).

* ``DELETE:`` Remove the resource (Section 9.3.5).

* ``HEAD:`` Retrieve headers only (Section 9.3.2).

* ``OPTIONS:`` Retrieve communication options (Section 9.3.7).

These methods are part of the core semantics, ensuring a uniform interface as described in Section 1.3 of RFC 9110.

**Headers and Metadata:**

Headers, detailed in Section 6.3 of RFC 9110, are key-value pairs providing metadata about the request or response.
They include information like content type (Content-Type), length (Content-Length), and caching directives
(Cache-Control). New field values must follow ABNF from `RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110>`__ or
`RFC 8941 <https://www.rfc-editor.org/rfc/rfc8941>`__: Structured Field Values for HTTP, ensuring compatibility and
extensibility.

**Status Codes:**

Responses include three-digit status codes, as outlined in
`Section 15 of RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110#name-status-codes>`_, indicating the request's outcome.

Examples include:

* ``200 OK``: Successful request.

* ``404 Not Found``: Resource unavailable.

* ``500 Internal Server Error``: Server-side issue.

These codes, along with optional reason phrases, form the start line of responses, as per Section 6.2.

**Message Body and Representations:**

The message body, as described in `Section 6.4 of RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110#name-content>`_,
contains the representation data, such as HTML, images, or JSON, reflecting the resource's state. Representations are
central to HTTP's uniform interface, enabling content negotiation, detailed in
`Section 12 of RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110#name-content-negotiation>`_, where clients and servers
agree on format and language via headers like Accept and Accept-Language.

**Message Format:**

HTTP messages, as per `Section 3.4 of RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110#name-messages>`_ and
`Section 6 of RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110#name-message-abstraction>`_, consist of a start line,
headers, an optional body, and trailers. For requests, the start line includes the method, request target, and HTTP
version; for responses, it includes the version, status code, and reason phrase. The format supports framing, with
modern versions using length-delimited sequences, as noted in
`Section 6.1 of RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110#name-framing-and-completeness>`_, moving away from
connection closure in early versions like ``HTTP/0.9``.

Evolution and Versions
----------------------

HTTP has evolved significantly since its inception, with versions enhancing performance and functionality. The history,
as outlined in `Section 1.2 of RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110#name-history-and-evolution>`_, shows:

**HTTP/1.1:**

Defined in `RFC 9112: HTTP/1.1 <https://www.rfc-editor.org/rfc/rfc9112>`_, it introduced persistent connections,
chunked transfer encoding, and refined caching mechanisms, standardizing features from 1995 and revised in 2014.

**HTTP/2:**

Specified in `RFC 9113: HTTP/2 <https://www.rfc-editor.org/rfc/rfc9113>`_, it added multiplexing for concurrent
requests, header compression using HPACK (RFC 7541), and server push, improving efficiency over TCP and TLS.

**HTTP/3:**

Detailed in `RFC 9114: HTTP/3 <https://www.rfc-editor.org/rfc/rfc9114>`_, it uses the QUIC transport protocol over UDP,
offering stream multiplexing, per-stream flow control, and low-latency connection establishment, enhancing performance
and reliability.


All versions share core semantics from `RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110>`_, with separate documents
for caching (`RFC 9111 <https://www.rfc-editor.org/rfc/rfc9111>`_) and specific version syntax, allowing independent
progression as noted in the history section.

Additional Features and Security
--------------------------------

HTTP includes mechanisms for caching, as per `RFC 9111 <https://www.rfc-editor.org/rfc/rfc9111>`_, controlled by
headers like Cache-Control, ETag, and Last-Modified, enabling clients and intermediaries to store responses, reducing
latency and server load. Content negotiation, as mentioned, enhances flexibility, while security is addressed through
HTTPS, HTTP over TLS, as referenced in RFCs like `RFC 5246: TLS 1.2 <https://www.rfc-editor.org/rfc/rfc5246>`_ and
`RFC 8446: TLS 1.3 <https://www.rfc-editor.org/rfc/rfc8446>`_, encrypting data to protect against eavesdropping and
tampering.

Comprehensive Table of RFC Specifications
-----------------------------------------

Below is a table summarizing the key RFCs relevant to HTTP, ensuring a complete reference for documentation:


+-------------------------------------------------------+----------------+------------------------------------+------------+
| RFC                                                   | Title          | Description                        | Status     |
+=======================================================+================+====================================+============+
| `RFC 9110 <https://www.rfc-editor.org/rfc/rfc9110>`_  | HTTP Semantics | Defines core protocol elements,    | Internet   |
|                                                       |                | extensibility, and URI schemes,    | Standard   |
|                                                       |                | obsoleting RFCs 2818, 7231, etc.   |            |
+-------------------------------------------------------+----------------+------------------------------------+------------+
| `RFC 9111 <https://www.rfc-editor.org/rfc/rfc9111>`_  | HTTP Caching   | Details caching mechanisms,        | Internet   |
|                                                       |                | enhancing efficiency.              | Standard   |
|                                                       |                |                                    |            |
+-------------------------------------------------------+----------------+------------------------------------+------------+
| `RFC 9112 <https://www.rfc-editor.org/rfc/rfc9112>`_  | HTTP/1.1       | Specifies message syntax, parsing, | Internet   |
|                                                       |                | and connection management for      | Standard   |
|                                                       |                | HTTP/1.1.                          |            |
+-------------------------------------------------------+----------------+------------------------------------+------------+
| `RFC 9113 <https://www.rfc-editor.org/rfc/rfc9112>`_  | HTTP/2         | Describes optimized semantics with | Proposed   |
|                                                       |                | multiplexing and compression,      | Standard   |
|                                                       |                | obsoleting RFC 7540.               |            |
+-------------------------------------------------------+----------------+------------------------------------+------------+
| `RFC 9114 <https://www.rfc-editor.org/rfc/rfc9112>`_  | HTTP/3         | Maps HTTP semantics over QUIC,     | Proposed   |
|                                                       |                | enhancing performance with low     | Standard   |
|                                                       |                | latency.                           |            |
+-------------------------------------------------------+----------------+------------------------------------+------------+
| `RFC 8941 <https://www.rfc-editor.org/rfc/rfc9112>`_  | Structured     | Defines field value syntax for     | Proposed   |
|                                                       | Field Values   | headers, used in RFC 9110.         | Standard   |
|                                                       | for HTTP       |                                    |            |
+-------------------------------------------------------+----------------+------------------------------------+------------+
| `RFC 7541 <https://www.rfc-editor.org/rfc/rfc9112>`_  | HPACK: Header  | Details header compression for     | Standards  |
|                                                       | Compression    | HTTP/2, enhancing efficiency.      | Track      |
|                                                       | for HTTP/2     |                                    |            |
+-------------------------------------------------------+----------------+------------------------------------+------------+
| `RFC 5246 <https://www.rfc-editor.org/rfc/rfc9112>`_  | TLS Protocol   | Supports secure HTTP via TLS,      | Proposed   |
|                                                       | Version 1.2    | referenced for HTTPS.              | Standard   |
+-------------------------------------------------------+----------------+------------------------------------+------------+
| `RFC 8446 <https://www.rfc-editor.org/rfc/rfc9112>`_  | TLS Protocol   | Latest TLS version, enhancing      | Proposed   |
|                                                       | Version 1.3    | HTTPS security.                    | Standard   |
+-------------------------------------------------------+----------------+------------------------------------+------------+


The goal of this project is providing test features and support objects to be compatible with the mentioned RFCs.

