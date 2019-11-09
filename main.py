from setting import UA
import random
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import time
# 利用twilio网站向手机发送短信
url = 'https://www.apple.com/cn/shop/refurbished/ipad/10-5-%E8%8B%B1%E5%AF%B8-ipad-pro'


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'geo=CN; ccl=F/wvqOVFk3tX0Wh/xKNP0Q==; s_fid=0B429A1184ECD7B3-16B39A6E2301BCFC; s_cc=true; s_vi=[CS]v1|2ED806A085158000-40148B0B078CE86D[CE]; dssid2=7091427b-c93a-4b4e-967d-9619ef0f43d7; dssf=1; optimizelyEndUserId=oeu1572306127350r0.32303250844229625; optimizelyBuckets=%7B%7D; pxro=1; xp_ci=3zNQpINzCMoz5K7zBr6zI5sYJqgS; check=true; as_loc=b2cfd5b0305207bd6816abc01dacbe45c3d7f0b426f5d3cae72259e13678bd2d92ba83d79efef06c782917a8330bf38b0400b3d3ea468744a0c38cb0be7ab693a681adf5d819ad91eaf341a22bc545a09df913fcf6a94b4ad3e15831b58e53db994bd86589510794672ed2e6640230b6e251b9322d816c0f9c0f4ea91a9de080; as_cn=~0i1DvjwdI16ZyEWgaGEK2rtKP7Hf_OP-l-gDGHSQHG0=; optimizelySegments=%7B%22341793217%22%3A%22referral%22%2C%22341794206%22%3A%22false%22%2C%22341824156%22%3A%22gc%22%2C%22341932127%22%3A%22none%22%2C%22381100110%22%3A%22gc%22%2C%22381740105%22%3A%22none%22%2C%22382310071%22%3A%22referral%22%2C%22382310072%22%3A%22false%22%7D; as_affl=p238%7C%7Cmtid%3A%3A18707vxu38484%26mnid%3A%3A1XbDdG5pN-dc_mtid_18707vxu38484_pcrid_20277607094_%26cid%3A%3Aaos-cn-kwba-btb%26%7C%7C20191104_001016; s_campaign=aos-cn-kwba-btb; s_afc=p238%7C1XbDdG5pN-dc_mtid_18707vxu38484_pcrid_20277607094_; as_pcts=38_rHVpmX1TLGKknB9x1Y+_6X_wQog6cdkv+:Fpxdq:guqQ-2oKV2-d_4y-6Rznh_mAImSnVPlzxeDrTI; s_orientation=%5B%5BB%5D%5D; s_vnum_n2_cn=4%7C1; as_xs=; as_xsm=; ac_history=%7B%22search%22%3A%5B%5D%2C%22kb%22%3A%5B%5D%2C%22help%22%3A%5B%5D%2C%22psp%22%3A%5B%5D%2C%22offer_reason%22%3A%7B%7D%2C%22total_count%22%3A%7B%7D%7D; accs=o; POD=us~en; s_ppvl=acs%253A%253Apsp%253A%253Aipad%253A%253Alanding%2520%2528en-us%2529%2520%2C21%2C21%2C920%2C1904%2C920%2C1920%2C1080%2C1%2CP; s_ppv=acs%253A%253Apsp%253A%253Aipad%253A%253Alanding%2520%2528en-us%2529%2520%2C60%2C19%2C2920%2C1904%2C920%2C1920%2C1080%2C1%2CP; s_orientationHeight=2020; s_vnum_n2_us=4%7C6; as_ltn_cn=1aosZb4WwJLod/L%2Bt1A59Rp93z/zVZxF%2BiEnDEDe35fdLEPh1WVQB8ooaIGUWDUB51ydxtcmoV93q/wlpPH18SVKCKITpL0qlQdcGf4j7NVm6F668TGmjOLBgZDw9fTNCp97RtajlSRTB8UMnYX41/0/WhW5YH1lX1OeNPQl6cj7hub9Hbcfit2XGz8NVH0d2xFC%2B3cspVgLNYyyRN0jBeyyEA%3D%3D; as_atb=1.0|MjAxOS0xMS0wOCAwODoyODozNA|f9a677a1ba51965d2915b71681643ddc020e3cfc; mbox=PC#ea1b3c64ee1d4ccdb1e0c83b48005f75.22_21#1636523596|session#020c94267daa43d0a099fe3a15410607#1573280656; s_ptc=0.018%5E%5E0.000%5E%5E0.000%5E%5E0.000%5E%5E0.004%5E%5E0.004%5E%5E0.359%5E%5E0.005%5E%5E0.789%5E%5E1.156%5E%5E0.000%5E%5E1.186; s_aca_ct=; dslang=US-EN; site=USA; acn01=1TZ7W490KLDIyZBtBxL9xGesf7jpdG2nAAVhEjFfu20=; as_disa=AAAjAAABxhvK-54AO5VzZVsDBRMrayA1weH9QUBCd9kMD1B-M46weZiURBd-jdUmJSgA3IxoAAIBxFrmlIjjco4815cLIu2mwHO4T9rscUEkGe1QJE2Wg30=; as_rec=06050c7206bd13b2cd6b5ef0b5f0edb76c846bb92a638059bbb817d44e79fd0320bdf4cf57e3739eccdd6b3150a05d3ea0f666d13d2f56c819aaf400493eb88fbfb0fbae8801528dad06139b60d179a0; as_ltn_us=1aosx1mGMBwcLhlct7CMcjVbG4ovJt1LVbtHo9imBrFPzJ36Cw1pQswOrfYcXZ96yIsqWD7Uunlv0Wws0SPE8oA8Xyg5yWcmU4psp03mRt7c5uVa5p98KZG5QCaTXEwmFJJtWvFt8FgUmzJlM0eEf%2BhE4oAT4F1cLtrO3S7Q6HywCCJasJ9DLpyb0%2BTpFDQW1JCq8Qgk4MDKfxRCUHpx0foi5g%3D%3D; s_sq=appleusother%3D%2526c.%2526a.%2526activitymap.%2526page%253Dchoose%252520your%252520country%252520-%252520index%252520%252528us%252529%2526link%253D%2525E4%2525B8%2525AD%2525E5%25259B%2525BD%2525E5%2525A4%2525A7%2525E9%252599%252586%252520-%252520%25252Fcn%25252F%252520-%252520asia-pacific%2526region%253Dasia-pacific%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dchoose%252520your%252520country%252520-%252520index%252520%252528us%252529%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.apple.com%25252Fcn%25252F%2526ot%253DA; as_dc=nc; as_sfa=Mnxjbnxjbnx8emhfQ058Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE=; as_metrics=%7B%7D',
    'pragma': 'no-cache',
    'referer': 'https://www.apple.com/cn/shop/refurbished',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent':UA[random.randint(0, len(UA) - 1)],
}
response = requests.get(url = url, headers = headers)
soup = BeautifulSoup(response.text,'html.parser')
text = ""

for s in soup.select(".as-price-currentprice"):
    if s.text.split()[-1:][0] == "4,603":
        text = "ddd"


active_number = '+12013081942'
my_phone_number = "13092378929"

account_sid = 'AC2b88fde0127597ebf64de7adb7349919'
auth_token = 'a60949cac18a507b0b6b6c55799f8e89'

client = Client(account_sid,auth_token)

def sent_message(phone_number):
    mes = client.messages.create(
        from_= active_number,
        body = text,
        to = phone_number
    )
    print("OK")

if(text != ""):
    sent_message("+86" + my_phone_number)
