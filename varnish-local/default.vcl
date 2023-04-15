vcl 4.1;

backend nginx_infoboard_cms {
    .host = "nginx_infoboard_cms";
    .port = "8082";
}

backend nginx_infoboard_front {
    .host = "nginx_infoboard_front";
    .port = "8081";
}

sub vcl_recv {
        if (req.http.host == "cms.infoboard-local.wronamichal.pl") {
            set req.http.host = "cms.infoboard-local.wronamichal.pl";
            set req.backend_hint = nginx_infoboard_cms;
        } elsif (req.http.host == "infoboard-local.wronamichal.pl") {
            set req.http.host = "infoboard-local.wronamichal.pl";
            set req.backend_hint = nginx_infoboard_front;
        } else {
            return(synth(500));
        }

        if (req.url ~ "^[^?]*\.(7z|avi|bmp|bz2|css|csv|doc|docx|eot|flac|flv|gif|gz|ico|jpeg|jpg|js|less|mka|mkv|mov|mp3|mp4|mpeg|mpg|odt|ogg|ogm|opus|otf|pdf|png|ppt|pptx|rar|rtf|svg|svgz|swf|tar|tbz|tgz|ttf|txt|txz|wav|webm|webp|woff|woff2|xls|xlsx|xml|xz|zip)(\?.*)?$") {
            unset req.http.Cookie;
            unset req.http.Authorization;
            return(hash);
        }
        if (req.method != "GET") {
            return (pass);
        }
        return(hash);
    }


sub vcl_backend_response {
    if (bereq.url ~ "^[^?]*\.(7z|avi|bmp|bz2|css|csv|doc|docx|eot|flac|flv|gif|gz|ico|jpeg|jpg|js|less|mka|mkv|mov|mp3|mp4|mpeg|mpg|odt|ogg|ogm|opus|otf|pdf|png|ppt|pptx|rar|rtf|svg|svgz|swf|tar|tbz|tgz|ttf|txt|txz|wav|webm|webp|woff|woff2|xls|xlsx|xml|xz|zip)(\?.*)?$") {
        unset beresp.http.Set-Cookie;
        set beresp.ttl = 1d;
    }
}