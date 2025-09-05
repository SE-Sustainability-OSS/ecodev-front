var dagfuncs = (window.dashAgGridFunctions = window.dashAgGridFunctions || {});

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

const iconGenerator = (icon, iconColor) => React.createElement('div',
    {
        style: {
            gap: '8px',
            paddingTop:'5px'
        }
    },
    [
        React.createElement(
            window.dash_iconify.DashIconify,
            {
                icon: icon,
                color: iconColor,
                height: '20px',
                style: {},
            },
        ),
    ]);

dagcomponentfuncs.DMC_Button = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData();
    }
    let leftIcon, rightIcon;
    if (props.leftIcon) {
        leftIcon = iconGenerator(props.leftIcon, props.color);
    }
    if (props.rightIcon) {
        rightIcon = iconGenerator(props.rightIcon, props.color);
    }
    return React.createElement(
        window.dash_mantine_components.Button,
        {
            onClick,
            variant: props.variant,
            color: props.color,
            leftSection: leftIcon,
            rightSection: rightIcon,
            radius: props.radius,
            style: {
                margin: props.margin,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                paddingLeft: '10px', 
                paddingRight: '0px', 
            },
        },
        props.value
    );
};
