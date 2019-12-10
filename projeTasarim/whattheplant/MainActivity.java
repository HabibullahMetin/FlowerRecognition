package com.gokhanbayram.whattheplant;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private Button btnWelcomeLogin, getBtnWelcomeRegister;

    public void init() {
        btnWelcomeLogin = (Button) findViewById(R.id.btnWelcomeLogin);
        getBtnWelcomeRegister = (Button) findViewById(R.id.btnWelcomeRegister);


    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();

        btnWelcomeLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intentLogin = new Intent(MainActivity.this,LoginActivity.class);
                startActivity(intentLogin);
                finish();
            }
        });

        getBtnWelcomeRegister.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                Intent intentRegister = new Intent(MainActivity.this,RegisterActivity.class);
                startActivity(intentRegister);
                finish();
            }
        });

    }
}
