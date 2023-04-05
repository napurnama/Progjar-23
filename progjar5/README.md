# Progjar-A-ETS-5025201195
Tugas ETS Progjar

## Insecure Multithreaded Server
* -c 10 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            8889

Document Path:          /testing.txt
Document Length:        4 bytes

Concurrency Level:      10
Time taken for tests:   141.880 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    7.05 [#/sec] (mean)
Time per request:       1418.804 [ms] (mean)
Time per request:       141.880 [ms] (mean, across all concurrent requests)
Transfer rate:          0.84 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       3
Processing:     5 1381 792.3   1347    5127
Waiting:        5 1364 783.1   1324    5031
Total:          6 1382 792.3   1347    5127

Percentage of the requests served within a certain time (ms)
  50%   1347
  66%   1716
  75%   1895
  80%   2007
  90%   2418
  95%   2721
  98%   3128
  99%   3536
```

* -c 50 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            8889

Document Path:          /testing.txt
Document Length:        4 bytes

Concurrency Level:      50
Time taken for tests:   383.594 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    2.61 [#/sec] (mean)
Time per request:       19179.720 [ms] (mean)
Time per request:       383.594 [ms] (mean, across all concurrent requests)
Transfer rate:          0.31 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       6
Processing:   715 18448 4444.1  18948   26686
Waiting:      641 18398 4434.8  18916   26534
Total:        715 18449 4444.2  18948   26686

Percentage of the requests served within a certain time (ms)
  50%  18948
  66%  20266
  75%  21740
  80%  22356
  90%  23667
  95%  24622
  98%  25474
  99%  25779
 100%  26686 (longest request)
```

* -c 100 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            8889

Document Path:          /testing.txt
Document Length:        4 bytes

Concurrency Level:      100
Time taken for tests:   650.370 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    1.54 [#/sec] (mean)
Time per request:       65037.043 [ms] (mean)
Time per request:       650.370 [ms] (mean, across all concurrent requests)
Transfer rate:          0.18 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       3
Processing:   791 61329 13447.7  64063   78396
Waiting:      766 61258 13442.1  63973   78238
Total:        791 61329 13447.7  64063   78396

Percentage of the requests served within a certain time (ms)
  50%  64063
  66%  66121
  75%  68606
  80%  69844
  90%  73880
  95%  75901
  98%  77316
  99%  77824
 100%  78396 (longest request)
```

* -c 150 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            8889

Document Path:          /testing.txt
Document Length:        4 bytes

Concurrency Level:      150
Time taken for tests:   137.470 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    7.27 [#/sec] (mean)
Time per request:       20620.527 [ms] (mean)
Time per request:       137.470 [ms] (mean, across all concurrent requests)
Transfer rate:          0.87 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       2
Processing:    29 17556 10907.4  18242   36659
Waiting:        5 17540 10898.9  18228   36659
Total:         30 17556 10907.4  18242   36659

Percentage of the requests served within a certain time (ms)
  50%  18242
  66%  23870
  75%  25992
  80%  27802
  90%  33249
  95%  35096
  98%  36027
  99%  36297
 100%  36659 (longest request)
 ```

* -c 200 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            8889

Document Path:          /testing.txt
Document Length:        4 bytes

Concurrency Level:      200
Time taken for tests:   142.571 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    7.01 [#/sec] (mean)
Time per request:       28514.169 [ms] (mean)
Time per request:       142.571 [ms] (mean, across all concurrent requests)
Transfer rate:          0.84 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       5
Processing:    50 23260 14623.2  23631   48377
Waiting:        4 23242 14614.5  23610   48241
Total:         50 23260 14623.3  23632   48378

Percentage of the requests served within a certain time (ms)
  50%  23632
  66%  30647
  75%  36623
  80%  39108
  90%  43472
  95%  44784
  98%  46416
  99%  47265
 100%  48378 (longest request)
 ```

## Secure Multithreaded Server
* -c 10 -n 1000

```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            7777
SSL/TLS Protocol:       TLSv1.3,TLS_AES_256_GCM_SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /testing.txt
Document Length:        Variable

Concurrency Level:      10
Time taken for tests:   194.659 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Keep-Alive requests:    0
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    5.14 [#/sec] (mean)
Time per request:       1946.589 [ms] (mean)
Time per request:       194.659 [ms] (mean, across all concurrent requests)
Transfer rate:          0.61 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       19 1266 703.1   1170    3399
Processing:    17  646 387.8    604    2445
Waiting:        8  621 376.8    577    2431
Total:         36 1911 1019.1   1825    5358

Percentage of the requests served within a certain time (ms)
  50%   1825
  66%   2295
  75%   2711
  80%   2894
  90%   3320
  95%   3664
  98%   3987
  99%   4239
 100%   5358 (longest request)
```

* -c 50 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            7777
SSL/TLS Protocol:       TLSv1.3,TLS_AES_256_GCM_SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /testing.txt
Document Length:        Variable

Concurrency Level:      50
Time taken for tests:   192.014 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Keep-Alive requests:    0
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    5.21 [#/sec] (mean)
Time per request:       9600.714 [ms] (mean)
Time per request:       192.014 [ms] (mean, across all concurrent requests)
Transfer rate:          0.62 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       16 8440 4515.1   8650   17213
Processing:    16  646 404.8    594    2378
Waiting:        5  621 393.0    572    2342
Total:         62 9086 4849.1   9404   18391

Percentage of the requests served within a certain time (ms)
  50%   9404
  66%  12056
  75%  12677
  80%  13175
  90%  15195
  95%  17369
  98%  17937
  99%  18184
 100%  18391 (longest request)
 ```

* -c 100 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            7777
SSL/TLS Protocol:       TLSv1.3,TLS_AES_256_GCM_SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /testing.txt
Document Length:        Variable

Concurrency Level:      100
Time taken for tests:   193.725 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Keep-Alive requests:    0
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    5.16 [#/sec] (mean)
Time per request:       19372.457 [ms] (mean)
Time per request:       193.725 [ms] (mean, across all concurrent requests)
Transfer rate:          0.62 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       15 16841 9208.1  17091   33264
Processing:    20  636 385.5    563    2373
Waiting:        6  609 375.4    540    2371
Total:        107 17476 9520.1  17815   34575

Percentage of the requests served within a certain time (ms)
  50%  17815
  66%  21185
  75%  25366
  80%  27102
  90%  31745
  95%  33276
  98%  33737
  99%  33965
 100%  34575 (longest request)
 ```

* -c 150 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            7777
SSL/TLS Protocol:       TLSv1.3,TLS_AES_256_GCM_SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /testing.txt
Document Length:        Variable

Concurrency Level:      150
Time taken for tests:   183.588 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Keep-Alive requests:    0
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    5.45 [#/sec] (mean)
Time per request:       27538.238 [ms] (mean)
Time per request:       183.588 [ms] (mean, across all concurrent requests)
Transfer rate:          0.65 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       16 23104 13481.8  22168   45168
Processing:    33  613 364.0    567    2133
Waiting:        7  590 354.2    539    2132
Total:        157 23716 13783.1  23040   46819

Percentage of the requests served within a certain time (ms)
  50%  23040
  66%  32368
  75%  35201
  80%  37901
  90%  43695
  95%  45016
  98%  45647
  99%  46001
 100%  46819 (longest request)
 ```

* -c 200 -n 1000
```
Server Software:        myserver/1.0
Server Hostname:        localhost
Server Port:            7777
SSL/TLS Protocol:       TLSv1.3,TLS_AES_256_GCM_SHA384,2048,256
Server Temp Key:        X25519 253 bits
TLS Server Name:        localhost

Document Path:          /testing.txt
Document Length:        Variable

Concurrency Level:      200
Time taken for tests:   200.966 seconds
Complete requests:      1000
Failed requests:        0
Non-2xx responses:      1000
Keep-Alive requests:    0
Total transferred:      122000 bytes
HTML transferred:       4000 bytes
Requests per second:    4.98 [#/sec] (mean)
Time per request:       40193.118 [ms] (mean)
Time per request:       200.966 [ms] (mean, across all concurrent requests)
Transfer rate:          0.59 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       16 32339 18483.4  32367   64045
Processing:    21  709 424.6    643    3158
Waiting:        7  684 415.2    625    3105
Total:        190 33048 18800.8  32894   65304

Percentage of the requests served within a certain time (ms)
  50%  32894
  66%  45224
  75%  50573
  80%  52238
  90%  57738
  95%  61963
  98%  63474
  99%  63919
 100%  65304 (longest request)
 ```

## Insecure Multiprocess Server
* -c 10 -n 1000
* -c 50 -n 1000
* -c 100 -n 1000
* -c 150 -n 1000
* -c 200 -n 1000

## Secure Multiprocess Server

