# http://www.karoltomala.com/blog/?p=592
# 
# reddy think : 
# https://r3---sn-ovgq0oxu-5goe.googlevideo.com/videoplayback?sparams=clen,dur,ei,gir,id,initcwndbps,ip,ipbits,itag,keepalive,lmt,mime,mm,mn,ms,mv,pl,requiressl,source,upn,expire&mv=m&mt=1478264670&ms=au&ip=130.225.0.251&clen=3880715&mn=sn-ovgq0oxu-5goe&mm=31&keepalive=yes&id=o-ALXgYG-X9O9yAesTtXhtIRwkN1wbzAbGqTDk6RNQyJU8&upn=kOtf8iSN_m4&source=youtube&itag=140&ei=BIgcWJc70PA0x-Sg4Ag&pl=26&lmt=1454579425365431&expire=1478286436&dur=244.297&ipbits=0&key=yt6&mime=audio/mp4&gir=yes&requiressl=yes&initcwndbps=4461250&cpn=i1UF0ltRcFTQ9-Sb&alr=yes&ratebypass=yes&signature=04713C584B1EFD99F39F0B5034B4770287866E9F.0FE48895FE821D3D2A2CE8371D7E8C9729E8A5F2&c=WEB&cver=1.20161101
# 
# jay park (audio)
# https://r4---sn-ovgq0oxu-5goe.googlevideo.com/videoplayback?sparams=clen,dur,ei,gcr,gir,id,initcwndbps,ip,ipbits,itag,keepalive,lmt,mime,mm,mn,ms,mv,pl,requiressl,source,upn,expire&mime=audio/mp4&key=yt6&ip=130.225.0.251&expire=1478287656&dur=249.103&lmt=1458197131857094&keepalive=yes&itag=140&requiressl=yes&clen=3956998&ipbits=0&upn=ahlIFigQPaA&pl=26&ei=yIwcWJm_GtWdd-KSvFA&source=youtube&gcr=dk&ms=au&mt=1478265928&mv=m&id=o-AHFmYU8BG382MblWxaoFYLBQVnK0xdfiPWX_HQrifgmK&gir=yes&mm=31&mn=sn-ovgq0oxu-5goe&initcwndbps=5142500&cpn=DaQMdnedtU9gSROx&alr=yes&ratebypass=yes&signature=4EF7ABFCB32419CFA3374057D80F87CFCC6FF0FB.A17B02676C8AB225321B29BF422221879515A8D2&c=WEB&cver=1.20161101&rn=0&rbuf=0
# 
# jay park (video)
# https://r4---sn-ovgq0oxu-5goe.googlevideo.com/videoplayback?sparams=clen,dur,ei,gcr,gir,id,initcwndbps,ip,ipbits,itag,keepalive,lmt,mime,mm,mn,ms,mv,pl,requiressl,source,upn,expire&mime=video/mp4&key=yt6&ip=130.225.0.251&expire=1478287656&dur=249.040&lmt=1458197909892980&keepalive=yes&itag=134&requiressl=yes&clen=17408349&ipbits=0&upn=ahlIFigQPaA&pl=26&ei=yIwcWJm_GtWdd-KSvFA&source=youtube&gcr=dk&ms=au&mt=1478265928&mv=m&id=o-AHFmYU8BG382MblWxaoFYLBQVnK0xdfiPWX_HQrifgmK&gir=yes&mm=31&mn=sn-ovgq0oxu-5goe&initcwndbps=5142500&cpn=DaQMdnedtU9gSROx&alr=yes&ratebypass=yes&signature=BCB0331D989CC5B2FC0889DB4F3850EDF6423EFD.D0FAF35172B6649AA6AF133F19014CB6F7E3E419&c=WEB&cver=1.20161101&rn=1&rbuf=0

import urllib 
import sys 
# import requests

# WHAT is AppURLopener?
class AppURLopener(urllib.FancyURLopener): 
	version = "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101230 Mandriva Linux/1.9.2.13-0.2mdv2010.2 (2010.2) Firefox/3.6.13"

if len(sys.argv) < 2: 
	print 'Usage : {prog} URL'.format(prog=sys.argv[0])
	video_id = 'UsaJsymfuWU'
	# sys.exit(1) # WHAT is exit 1?
else: 
	video_id = sys.argv[1]

# connect to the video 
opener = AppURLopener()
fp = opener.open('http://www.youtube.com/get_video_info?video_id={vid}'.format(vid = video_id))
data = urllib.unquote(urllib.unquote(fp.read()))
fp.close()
# TODO : what does data get?

if data.startswith('status=fail'): 
	print 'Error : Video not found!'
	sys.exit(2) # WHAT is exit 2?

# TODO 
# connect to the url and wait until the GET request 
# find the audio link from the GET request 
# probably..play?


# TODO : get the link
link = "https://r3---sn-ovgq0oxu-5goe.googlevideo.com/videoplayback?sparams=clen,dur,ei,gir,id,initcwndbps,ip,ipbits,itag,keepalive,lmt,mime,mm,mn,ms,mv,pl,requiressl,source,upn,expire&mv=m&mt=1478264670&ms=au&ip=130.225.0.251&clen=3880715&mn=sn-ovgq0oxu-5goe&mm=31&keepalive=yes&id=o-ALXgYG-X9O9yAesTtXhtIRwkN1wbzAbGqTDk6RNQyJU8&upn=kOtf8iSN_m4&source=youtube&itag=140&ei=BIgcWJc70PA0x-Sg4Ag&pl=26&lmt=1454579425365431&expire=1478286436&dur=244.297&ipbits=0&key=yt6&mime=audio/mp4&gir=yes&requiressl=yes&initcwndbps=4461250&cpn=i1UF0ltRcFTQ9-Sb&alr=yes&ratebypass=yes&signature=04713C584B1EFD99F39F0B5034B4770287866E9F.0FE48895FE821D3D2A2CE8371D7E8C9729E8A5F2&c=WEB&cver=1.20161101"

# read from the link 
fp = opener.open(link)
data = fp.read(1024)
while data:
	sys.stdout.write(data)
	data = fp.read(1024)
fp.close()









