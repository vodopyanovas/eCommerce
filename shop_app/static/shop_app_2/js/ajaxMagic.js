/**
 * Created by falcon178 on 16.12.2016.
 */
/**
  * Version: 1.0
  * Author: Anton Vodopyanov

  AJAX Magic


  1. Add to cart




**/
  /* ----------------------------------------------------------- */
  /*  1. Add to Cart
  /* ----------------------------------------------------------- */

    function ajaxAdd(add_url) {

            $.ajax({
                url: add_url,
                success: function (response) {
                    alert(response);

                    // $.ajax({
                    //     url: '/cart/',
                    //     success: function () {
                    //         $("#cart-item").load();
                    //     },
                    //    error: function () {
                    //        alert("Couldn't load");
                    //    }
                    // });
                },
                error: function () {
                    alert("Couldn't add item");
                }
            });
        }


    function ajaxDel(del_url) {

        $.ajax({
            url: del_url,
            success: function (response) {
                // alert(response);
            },
            error: function () {
                alert("Couldn't del item");
            }
        });
    }

jQuery(function($) {
    $(document).ready(function () {
        $(".aa-cart-notify").change(function () {
            alert("Changed!")
        });

        $("#item-del").click(function () {
            $("#cart-item").hide();
        });




        // $(".aa-add-card-btn").click(function () {
        //
        //     $.ajax({
        //         url: '/items-counter/',
        //         success: function () {
        //             $('.aa-cart-notify').load();
        //             // alert('Счётчик');
        //         },
        //         error: function () {
        //             alert("Erro");
        //         }
        //     });
        // });

    })
});


