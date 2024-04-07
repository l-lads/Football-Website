$(document).ready(function() {
    $('.dropdown').hover(
        function() {
            $(this).find('.dropdown-content').css('display', 'block');
        },
        function() {
            $(this).find('.dropdown-content').css('display', 'none');
        }
    );

    $('.nested-dropdown').hover(
        function() {
            var nestedDropdownContent = $(this).find('.nested-dropdown-content');
            var dropdownOffset = $(this).offset();
            var topPosition = dropdownOffset.top - 59.5;
            nestedDropdownContent.css({
                'display': 'block',
                'top': topPosition
            });
        },
        function() {
            $(this).find('.nested-dropdown-content').css('display', 'none');
        }
    );

    $('.standings').hover(
        function() {
            $(this).find('.standings-dropdown').css('display', 'block');
        },
        function() {
            $(this).find('.standings-dropdown').css('display', 'none');
        }
    );

    $('.fixtures').hover(
        function() {
            $(this).find('.fixtures-dropdown').css('display', 'block');
        },
        function() {
            $(this).find('.fixtures-dropdown').css('display', 'none');
        }
    );
});
