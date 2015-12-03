// http://md5online.net/
// HINT   |  Only query2[8] has more than one character.
document.getElementById("panel").onclick = function() {
    document.getElementById("message").innerHTML = "Checking...";
    setTimeout(function() {
        try {
            console.log(location.search.length);
            if (location.search.length != 25) throw Error();
            console.log("Checkpoint 1");
            var query = location.search.substring(1).split(/{|}/); // Split by { or }
            if (query[2]) throw Error();
            console.log("Checkpoint 2");
            var message = ("The " + query[0] + " is a string.").split(" ");
            var query2 = query[1].split("$");
            // Check calculate.py for code that calculates this
            if (query2[8].split("").map(function(k) {
                return k.charCodeAt(0);
            }).reduce(function(y, n) {
                return y + Math.pow(n ^ 95, 4);
            }) != 3111809) throw Error();
            console.log("Checkpoint 3");
            for (var i in message) {
                if (i != false) {
                    var q = message.splice(i, 1).join("");
                    var h = CryptoJS.MD5(message.splice(i + 1).join("") + message.join("%"));
                    var z = h.toString() + h.words.splice(0, 1);
                    break;
                }
            }
            var funcs = [String.fromCharCode, Object.getOwnPropertyNames, function(x) {
                // If x is equal to query2[2], return 3, otherwise return x
                // Used to get "r3v3rse"
                // Thus, since we want to replace "e" with "3", query2[2] must be "e"
                return (x == query2[2]) ? 3 : x;
            },
            // We want each element of the array, when run under c, to yield "th1s" when combined
            // We want query2[4] to yield "t", 156 to yield "h", and so on.
            // Again, since the first element will be the base of the string,
            // query2[4] must be "t"
            function(c) {
                return [query2[4], 156, 230, (query2[6].charCodeAt(0) * 2)].reduce(c);
            }];
            var add = function(a, b) {
                return a + b;
            }
            var m = new MersenneTwister((funcs[0] + "" [(query2[0] / 21)]).split(/\s/).join("").split("").map(function(x) {
                return x.charCodeAt(0);
            }).reduce(add) + 160);

            var func1Prototypes = ["concat", "constructor", "copyWithin", "entries", "every", "fill", "filter", "find", "findIndex", "forEach", "includes", "indexOf", "join", "keys", "lastIndexOf", "length", "map", "pop", "push", "reduce", "reduceRight", "reverse", "shift", "slice", "some", "sort", "splice", "toLocaleString", "toString", "unshift"]

            // something.join(_)
            // string[0] must give r3v3rse
            // string[1] must give th1s
            // string[2] must give str1ng
            // query2[3].charCodeAt(0) + 15 must yield 95, since that's the char code of _
            // Thus, query2[3][0] must be "P"
            var string = [
                // Takes first 6 chars of something from func1Prototypes and runs function(n)
                (function(n) {
                    // We want to call funcs[2], so query2[5].charCodeAt(0) ^ 66 must be 2
                    // This means that query2[5] is @

                    // We also know that query2[6].charCodeAt(0) - query2[7].charCodeAt(0) must yield 1 if we want to preserve the last "e"
                    // Without any other information, we can only guess right now as to what query2[6] and query2[7] are. Let's assume "a" and "b"

                    // We also want to run the function on "reverse", which is at index 22 of func1Prototypes.
                    // This means that query2[1].charCodeAt(0) - 101 must yield 21
                    // This means that query2[1] is z
                    return n.split("").map(funcs[query2[5].charCodeAt(0) ^ 66]).join("") +
                    n.charAt(query2[6].charCodeAt(0) - query2[7].charCodeAt(0));
                    })(func1Prototypes[query2[1].charCodeAt(0) - 101].substring(0, 6)),

                // This must yield "th1s"
                // Other functions don't make any sense in this context, so yolo and hope query2[8].charCodeAt(1) - 114 is 3, which it does.
                // Either this is a coincidence and we are lucky, or this is part of the problem. Let's hope the latter
                // This calls funcs[3] using the next function as its parameter.
                // Since m is the base, the first element must be "t"
                funcs[query2[8].charCodeAt(1) - 114](function(m, n) {
                    console.log(m);
                    console.log(h.words);
                    return m + (funcs[0](n ^ h.words.splice(0, 1) & 255));
                    }),

                // This must yield "str1ng"
                // ((m.genrand_int32() * Math.sqrt(m.random())) & 255) ^ x on each element in the array must yield "str1ng" when joined together
                // We can set the seed manually up above, just gotta figure out what seed we want...
                // Run calculate.js to calculate the seed we need
                // It is highly likely that the seed is 4744.
                //
                // var m = new MersenneTwister((funcs[0] + "" [(query2[0] / 21)]).split(/\s/).join("").split("").map(function(x) {
                //     return x.charCodeAt(0);
                // }).reduce(add) + 160);
                //
                // This means that the total sum of the char codes for "function fromCharCode() { [native code] }" must yield 4584
                // Apparently I'm also dumb because the above code evaluates to this...
                // Anyways, now with that out of the way, we need to figure out what query2[0] is.
                // Let's use the random thing again and get what we need to make "1".
                // running idk() from calculate.js, query2[0] is 'b'
                [181, 78, 28, query2[0].charCodeAt(0), 225, 129].map(function(x) {
                    return funcs[0](((m.genrand_int32() * Math.sqrt(m.random())) & 255) ^ x);
                    }).join("")
            ].join(funcs[0](query2[3].charCodeAt(0) + 15));
            console.log(string);
            // if (CryptoJS.MD5(string).toString() == "0f957300a52431c2d0de0da9fc7223c9") {
            if (string == "r3v3rse_th1s_str1ng") {
                document.getElementById("message").innerHTML = "Correct!";
            } else {
                throw Error();
            }
        } catch (e) {
            console.log(e.stack);
            document.getElementById("message").innerHTML = "Nope. :(";
        }
        }, 1000);
    };

// Try reading my notes on this if you can.
// tl;dr, this was really annoying
//
// sctf{S$z$e$P$t$@$s$r$qu}
