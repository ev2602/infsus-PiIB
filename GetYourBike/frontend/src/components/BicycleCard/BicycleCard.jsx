import { Button, Card, CardActions, CardContent, TextField, Typography } from '@mui/material';
import * as React from 'react';
import { DateRangePicker } from '@mui/x-date-pickers-pro/DateRangePicker';
import 'react-datepicker/dist/react-datepicker.css';
import { useState } from 'react';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers-pro/AdapterDayjs';
import dayjs from 'dayjs';
import 'dayjs/locale/en';
import bicycleImg from './bicycle.jpg'


const highlightReservedDates = (date, reservedDates) => {
    if (!date) return false
    return reservedDates.includes(date.format('YYYY-MM-DD'));
};

const BicycleCard = ({bicycle, category} ) => {
    const [selectedDateRange, setSelectedDateRange] = useState([null, null]);

    const handleDateRangeChange = (dateRange) => {
        const [start, end] = dateRange;
        if (!highlightReservedDates(start, bicycle.reserved_dates) && !highlightReservedDates(end, bicycle.reserved_dates)) {
            setSelectedDateRange(dateRange);
        }
    };
    
    return(
        <Card sx={{
            height:"auto",
            width:"100%",
            marginBottom: "1px",

        }}>
            <CardContent>
                <img style={{ width: '100%', height: 'auto', objectFit: 'cover' }} src={bicycleImg} />
                <Typography>
                    {bicycle.model}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    {bicycle.brand}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Category: {category}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Price per Day: {bicycle.pricePerDay}€
                </Typography>
                <div>
                    <LocalizationProvider dateAdapter={AdapterDayjs}>
                        <DateRangePicker
                            startText="Check-in"
                            endText="Check-out"
                            value={selectedDateRange}
                            onChange={(newValue) => handleDateRangeChange(newValue)}
                            renderDay={(day, _value, DayComponentProps) => {
                                const date = dayjs(day);
                                const isReserved = highlightReservedDates(date, bicycle.reservedDates);
                                return (
                                    <div
                                        style={{
                                            ...DayComponentProps.style,
                                            backgroundColor: isReserved ? 'lightgray' : undefined,
                                            borderRadius: '50%',
                                            pointerEvents: isReserved ? 'none' : undefined,
                                            textDecoration: isReserved ? 'line-through' : 'none',
                                        }}
                                    >
                                        {date.date()}
                                    </div>
                                );
                            }}
                            shouldDisableDate={(day) => highlightReservedDates(dayjs(day), bicycle.reservedDates)}
                        />
                    </LocalizationProvider>
                </div>
            </CardContent>
            <CardActions>
                <Button size="small">Reserve</Button>
            </CardActions>

        </Card>
    )
}

export default BicycleCard