87MM 재입고 알람 서비스입니다.

제작동기 : 87MM 재입고 알람 SMS를 신청했는데 제대로 작동을 하지 않아서 제작하게 되었습니다.

==========

개발도중 발생한 문제

품절 여부를 스크레이핑하던 도중 html코드가 javascript로 동적으로 받아와 BeautifulSoup로는 파싱이 불가함.

그러던 도중
https://www.facebook.com/groups/codingeverybody/permalink/2602214939819026/

나와 비슷한 문제가 발생한 사람을 발견했고, 여기서 해결책을 찾으려 하였다.

댓글속 참고링크 : 
https://www.slideshare.net/wangwonLee/2018-datayanolja-moreeffectivewebcrawling?fbclid=IwAR0q6Hz0Oxaxu1NjYJu29wOcl1_ZkLVciuKDxN4OTeV1tvGcNxwU8QipIhE

우선 웹드라이버를 사용해보기로 하였다.
참고링크 : https://beomi.github.io/2017/02/27/HowToMakeWebCrawler-With-Selenium/


네트워크 분석 : 
http://87mm.co.kr/ind-script/optimizer.php?filename=tZRRbtswDIYPEL_2HIrbPmyPXdACQ4umS9ADKBIdK6ZElZKSeqef7GVbg3Ur7CQwDIOi_o8URP-iJguivGRRsbSwI24EQ6DECsQmCFN-csUmXIj_7UvGS9WIzUsCbvefsrjOz4HSM62z-IAfPBsXq483alLJgot3xHZGLjIhAr-vQ7MSzz97WrxBoPzeIkk9SGRTlNGQm68C8HZgRU_YVgbxfZH0Xixr8geSO86HEzOyltxzNMOlT0w6qXijten6ljjw-jymtXFBbCUaLSPxPlH8XjgaCK8RnA5_gzPBkwtwvgo1oIcznqCWTuM5C-QRNFV7Pn4e13iC_pGURBANjZ3fBWwN7Maqu_8nm8UfeQTre4aSqobe1nrMF5KsDzgNTe4XXa5Ydbmi_Dwtp1fldFp-bFI3KdbL5cPYrr85OcheZokZnGpFyNhJdlIFR-jVPppU2WJlPLaTU2HSGBN8hN2v0d4EcqP0-Z2ja0Zp577zXnH7Gln2oD7uwyWhphRPjX369-2Ph361ct1BfwA&type=js&k=3bd9ba54d4f499e4d7db016f2a90254d3eb0b16c&t=1546623004

handleTotalPrice : function(sOptionStockData, iProductPrice, sDispNonePrice, bButton, iManualQuantity) {
            var aStockData = $.parseJSON(sOptionStockData);
            var sOptionId = '';
            var iTotalPrice = 0;
            var iCnt = 1;
            var sQuantity = '('+sprintf(__('%s개'), iCnt)+')';
            var sPrice = '';

            // 옵션 선택 완료 되었을때 check
            var aOption = new Array();
            var aRequiredData = new Array();
            var sOptionText = '';
            var aOptionText = new Array();
            var bItemSelected = false, bSoldOut = false;
            var iTotalQuantity = 0;

            var aItemSelectInfo = Olnk.getOlnkSelectedItem(aStockData, bButton, sDispNonePrice, iProductPrice);

            bResult = aItemSelectInfo.bResult;
            bItemSelected = aItemSelectInfo.bItemSelected;
            aOption = aItemSelectInfo.aOption;
            if (aItemSelectInfo.sOptionId !== '') {
                sOptionId = aItemSelectInfo.sOptionId;
            }
            iTotalPrice = aItemSelectInfo.iTotalPrice;


            if (bItemSelected === true) {
                var sOptionText   = '';
                var iStockNumber  = aStockData[sOptionId].stock_number;
                var bStock        = aStockData[sOptionId].use_stock;
                var useSoldOut    = aStockData[sOptionId].use_soldout;
                var sIsDisplay    = aStockData[sOptionId].is_display;
                var sIsSelling    = aStockData[sOptionId].is_selling;
                var sIsReserveStat    = aStockData[sOptionId].is_reserve_stat; //예약주문R|Q당일발송

                var iBuyUnit  = EC_FRONT_NEW_PRODUCT_QUANTITY_VALID.getBuyUnitQuantity('base');
                var iProductMin = EC_FRONT_NEW_PRODUCT_QUANTITY_VALID.getProductMinQuantity();

                var iQuantity = (iBuyUnit >= iProductMin ? iBuyUnit : iProductMin);

                if (typeof(iManualQuantity) !== 'undefined') {
                    iQuantity = iManualQuantity;
                }
                if (sIsSelling == 'F' || ((iStockNumber < buy_unit || iStockNumber <= 0) && ( (bStock === true  && useSoldOut === 'T' ) || sIsDisplay == 'F'))) {
                    bSoldOut = true;
                    sOptionText =  ' <span class="soldOut">['+__('품절')+']</span>';
                }

                if (bSoldOut === true && isNewProductSkin() === false) {
                    alert(__('이 상품은 현재 재고가 부족하여 판매가 잠시 중단되고 있습니다.') + '\n\n' + __('제품명') + ' : ' + product_name );
                    return;
                }

                //( 품절 or 추가메시지)
                if (aReserveStockMessage['show_stock_message'] === 'T' && sIsReserveStat !== 'N') {
                    var sReserveStockMessage = '';
                    bSoldOut = false; //품절 사용 안함

                    sReserveStockMessage = aReserveStockMessage[sIsReserveStat];
                    sReserveStockMessage = sReserveStockMessage.replace(aReserveStockMessage['stock_message_replace_name'], iStockNumber);
                    sReserveStockMessage = sReserveStockMessage.replace('[:PRODUCT_STOCK:]', iStockNumber);

                    sOptionText = sOptionText.replace(sReserveStockMessage, '') + ' <span class="soldOut">'+sReserveStockMessage+'</span>';
                }

                // 옵션 선택시 재고 수량이 현재 선택되어진 수량보다 적을 경우 alert처리후에 return합니다.
                $('.option_box_id').each(function(i) {
                    iTotalQuantity += parseInt($('#' + $(this).attr('id').replace('id','quantity')).val());
                });

                if (iTotalQuantity > 0) {
                    iTotalQuantity += iQuantity;
                    if (((iStockNumber < iTotalQuantity || iStockNumber <= 0) && ((bStock === true  && useSoldOut === 'T' ) || sIsDisplay == 'F'))) {
                        alert(__('재고 수량이 부족하여 더 이상 옵션을 추가하실 수 없습니다.'));
                        return;
                    }
                }

                sOptionId = '';
                if ((Olnk.bAllSelectedOption === true || bButton === true) && aOption.length === 0) {
                    $('select[id^="' + product_option_id + '"]').each(function() {
                        sSelectedOptionId = $(this).attr('id');
                        sOptionId += $(this).val() + '_'+$(this).attr('option_code') +'||';
                    });
                    aOptionText.push( __('선택한 옵션 없음'));
                } else {
                    $('select[id^="' + product_option_id + '"]').each(function() {
                        if ($(this).attr('required') === false && $(this).val() === '*') {
                            return true;
                        }
                        if (Olnk.getCheckValue($(this).val(),'') === true) {
                            sSelectedOptionId = $(this).attr('id');
                            aOptionText.push( $('#'+sSelectedOptionId+ ' option:selected').text());
                        }
                        sOptionId += $(this).val() + '_'+$(this).attr('option_code') +'||';
                    });
                }

                iProductPrice = getProductPrice(iQuantity, iTotalPrice, sOptionId, bSoldOut, function(iProductPrice){
                    if (isNewProductSkin() === false) {
                        if (sIsDisplayNonmemberPrice == 'T') {
                            $('#span_product_price_text').html(sNonmemberPrice);
                        } else {
                            $('#span_product_price_text').html(SHOP_PRICE_FORMAT.toShopPrice(iProductPrice));
                        }
                    } else {
                        setOptionBox(sOptionId, (aOptionText.join('/')) + ' ' + sOptionText , iProductPrice, bSoldOut, sSelectedOptionId, sIsReserveStat, iManualQuantity);
                    }

                });


            }

        },