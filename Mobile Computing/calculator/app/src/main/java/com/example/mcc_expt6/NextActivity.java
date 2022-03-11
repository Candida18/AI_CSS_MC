package com.example.mcc_expt6;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class NextActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_next);

        TextView tv = findViewById(R.id.tv);

        String result = getIntent().getStringExtra("result");

        tv.setText("The output is " + result);
    }
}